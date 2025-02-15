# Gem5 Experiments

## Setup:

You will need to build GEM5 on a linux system to get this working.

Compile the Vector Addition Script into an exceutable, and then update the binary_path variable in the following line in the L1Experiment.py script.
```
binary_path = "ReplaceWithPathtoExceutable/vector_addition"
```

Afterwards, run GEM5 with this script as usual with
```
ReplaceWithPathtoGEM5/build/X86/gem5.opt ReplaceWithPathToScript/L1Experiment.py
```

## Why?

I was in the famous Yale Patt's ECE 460N Lecture and as he was talking about tradeoffs he mentioned CPU Caches being a prime example. 

I remember speaking to an AMD Research Engineer about how they were looking for someone with GEM5 Experience.

With this in mind, I figured it would be interesting to learn how to use GEM5 to test out what I had learned in computer architecture with as close to a real world situation as I could reasonably get.

I may also update this repository with additional CPU Configurations and tests for fun.

## What you can do with GEM5 (and by messing around with this script)

While this model CPU isn't particuarlly accurate, it can help provide some insights on to optimal CPU cache sizes and speeds at the cycle level with real world X86 programs.

I would encourage you if you are reading this to try it out for yourself, it can help provide some insights into why we don't have super large or super small L1 Cache sizes.

It's interesting to see how at least for this model "16kB for L1" and "64 kB for L1D" seems to be the sweetspot.

