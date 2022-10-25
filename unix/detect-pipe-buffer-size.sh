#!/usr/bin/env bash
#
# Write code to detect the default pipe buffer size.
#
# The shell starts the two programs in parallel but dd is really fast
# so when we send the signal it's blocked because the pipe buffer is
# full (you can use sleep to delay sending the signal).

dd if=/dev/zero bs=1k | killall -s SIGINT dd
