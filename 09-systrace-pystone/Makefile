all: trace.html

trace.html: test.py
	clear
	bash -c "../99-systrace/systrace -o $@ -t 3 -b 40960 ; xdg-open $@ "&
	bash -c "sleep 0.5 && time env ENABLE_SYSTRACE=1 python pystone.py"

clean:
	- rm -f trace.html
