import basic
import os
import sys
import tlang_decoder


if sys.argv[1] == "-s":
    print("To exit from the shell do exit()")
    while basic.repeate == "yes":
        basic.listen()
else:
    if sys.argv[1] == "-f":
        tlang_decoder.langcheck(sys.argv[2])

