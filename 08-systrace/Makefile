all: trace.html

trace.html: test.py
	clear
	bash -c "../99-systrace/systrace -o $@ ; xdg-open $@ "&
	bash -c "sleep 0.5 && time env ENABLE_SYSTRACE=1 python test.py"

clean:
	- rm -f trace.html
