all: trace.png

trace.log: pystone.py
	clear
	bash -c "time strace -o $@ -f -ttt -e trace=access,execve env ENABLE_PTRACE=1 python pystone.py 50"

trace.png: trace.log
	./drawplot $^ -o $@
	- xdg-open $@

diff:
	- diff -uN ../02-pystone-profile/pystone.py pystone.py

clean:
	- rm -f trace.png trace.log
