all: trace.html

trace.html: test.py
	bash -c "../99-systrace/systrace -o $@ -t 3 -b 20480 && gvfs-open $@ &" 
	bash -c "sleep 0.5 && time env ENABLE_SYSTRACE=1 python pystone.py 10000"

clean:
	- rm -f trace.html
