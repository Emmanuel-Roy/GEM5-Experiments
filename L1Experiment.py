import m5
from m5.objects import (
    System,
    Process,
    TimingSimpleCPU,
    SystemXBar,
    AddrRange,
    MemCtrl,
    DDR3_1600_8x8,
    VoltageDomain,
    SrcClockDomain,
    Cache,
    Root,
    SEWorkload
)

# L1 Instruction Cache
class L1ICache(Cache):
    def __init__(self, size='16kB'):
        super().__init__()
        self.size = size
        self.assoc = 2
        self.tag_latency = 2
        self.data_latency = 2
        self.response_latency = 2
        self.mshrs = 4
        self.tgts_per_mshr = 20
    # Connect Cache to CPU
    def connectCPU(self, cpu):
        cpu.icache_port = self.cpu_side

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

# L1 Data Cache
class L1DCache(Cache):
    def __init__(self, size='64kB'):
        super().__init__()
        self.size = size
        self.assoc = 2
        self.tag_latency = 2
        self.data_latency = 2
        self.response_latency = 2
        self.mshrs = 4
        self.tgts_per_mshr = 20
    # Connect Cache to CPU
    def connectCPU(self, cpu):
        cpu.dcache_port = self.cpu_side

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

# System
system = System()
system.clk_domain = SrcClockDomain(clock='1GHz', voltage_domain=VoltageDomain())
system.membus = SystemXBar()

# CPU and interrupt controller setup
system.cpu = TimingSimpleCPU()
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Caches and Memory Controller setup
system.l1_icache = L1ICache()
system.l1_dcache = L1DCache()
system.l1_icache.connectCPU(system.cpu)
system.l1_icache.connectBus(system.membus)
system.l1_dcache.connectCPU(system.cpu)
system.l1_dcache.connectBus(system.membus)

system.mem_ctrl = MemCtrl(dram=DDR3_1600_8x8(range=AddrRange('512MB')))
system.mem_ctrl.port = system.membus.mem_side_ports

for obj in system.descendants():
    if hasattr(obj, "mem_mode"):
        obj.mem_mode = "timing"

# Workload setup and Simulation start

binary_path = "/home/vboxuser/gem5/vector_addition"
system.workload = SEWorkload.init_compatible(binary_path)
process = Process(cmd=[binary_path])
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)
m5.instantiate()

print("Starting simulation...")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")

m5.stats.dump()
m5.stats.reset()
