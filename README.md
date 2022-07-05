# TaggedTimeLine

Author: Jaesun Park (GitHub: [@moran991231](https://github.com/moran991231))  
You can use and modify this for free.
## Intro
This is a kind of a stopwatch which has string tags.  
I made this for analyse the latencies step by step.  
```
|--step1--|----step2----|-----step3-----|--step4--|--...
^         ^             ^               ^         ^
|         |             |               |         |
init    step1         step2           step3     step4  ...

=>
step1: (the time interval between init  and step1)
step2: (the time interval between step1 and step2)
step3: (the time interval between step2 and step3)
step4: (the time interval between step3 and step4)
```

## Function
* linear analysis (no loop) => see the `ex_noloop()` in the `/example.py`
```
:::: Example Without Loop ::::
 My Daily Routine
sleeping...
having a lunch...
studying python...
attending a lecture...
having a dinner...

-- print all --
(1. sleep 1.0104 s) (2. have lunch 1.3005 s) (3. study python 1.0047 s) (4. attend a lecture 2.0022 s) (5. have dinner 1.0075 s) (total 6.3254 s)

-- print tag --
5. have dinner:1.0075s

-- print interval --
2. have lunch's end ~ 5. have dinner : 4.0144s
```
  

* Iteration analysis (loop) => see the `ex_loop()` in the `/example.py`

```
:::: Example With Loop ::::
 My Daily Routine

! loop !
sleeping...
having a lunch...
studying python...
attending a lecture...
having a dinner...
-- print all --
(1. sleep 1.0031 s) (2. have lunch 1.3004 s) (3. study python 1.0035 s) (4. attend a lecture 2.0137 s) (5. have dinner 1.0109 s) (total 6.3317 s)

! loop !
sleeping...
having a lunch...
studying python...
attending a lecture...
having a dinner...
-- print all --
(1. sleep 1.0088 s) (2. have lunch 1.3094 s) (3. study python 1.0052 s) (4. attend a lecture 2.0136 s) (5. have dinner 1.0044 s) (total 6.3414 s)

sleeping...
having a lunch...
studying python...
attending a lecture...
having a dinner...
-- print all --
(1. sleep 1.0077 s) (2. have lunch 1.3090 s) (3. study python 1.0089 s) (4. attend a lecture 2.0108 s) (5. have dinner 1.0032 s) (total 6.3395 s)

-- print avg --
The average of accumulated latency per loop:
 (1. sleep 1.0082 s)
 (2. have lunch 1.3092 s)
 (3. study python 1.0070 s)
 (4. attend a lecture 2.0122 s)
 (5. have dinner 1.0038 s)
 (total 6.3405 s)
```


## Usage
