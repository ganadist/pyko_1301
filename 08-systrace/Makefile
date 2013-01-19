all: trace.html

trace.html: test.py
	bash -c "../99-systrace/systrace -o $@ && gvfs-open $@ &" 
	bash -c "sleep 0.5 && time env ENABLE_SYSTRACE=1 python test.py"

clean:
	- rm -f trace.html
