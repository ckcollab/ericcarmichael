Title: Debug running process on Linux
Date: 2014-8-28 15:10
Category: web development
Tags: web development, development, dev ops


I am working on putting out a serious fire now. Gettin' into that weird head space where you grow as a developer,
the place where all hair is pulled out, desks are slammed, "WHAAT!?" is screamed every 45 minutes, but you
can't really force yourself to take a break.

I need to make sure this worker is running properly and the `stdout` output is all I need to get to the juicy debug info.

First I'll get the process ID

```
> ps -ef | grep worker
1000 2778 2308 0 Aug28 ? 00:00:03 /home/supertastic/worker.py
```

The process id in this case is `2778`, now let's use this snippet to watch on `-p 2778`

```
> sudo strace -f -e trace=write -e verbose=none -e write=1,2 -q -p 2778 -o "| grep '^ |' | cut -c11-60 | sed -e 's/ //g' | xxd -r -p"
2014-08-29 02:14:09,459 DEBUG Received message: {"task_type": "evaluate_submission"}
2014-08-29 02:14:09,460 INFO Running task: id=10131 task_type=evaluate_submission
2014-08-29 02:14:09,461 DEBUG evaluate_submission_task begins (job_id=10131)
2014-08-29 02:14:09,462 DEBUG evaluate_submission_task submission_id=9481 (job_id=10131)
```


Thanks to [Lari Hotari](http://stackoverflow.com/questions/249703/how-can-a-process-intercept-stdout-and-stderr-of-another-process-on-linux) for giving everyone a neat solution.

