all: trace.png

trace.log: test.py
	clear
	bash -c "time strace -o $@ -f -ttt -e trace=access,execve env ENABLE_PTRACE=1 python test.py"

trace.png: trace.log
	./drawplot $^ -o $@
	- xdg-open $@

clean:
	- rm -f trace.png trace.log
