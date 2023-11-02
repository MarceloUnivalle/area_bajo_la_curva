parallel: compile
	python3 area_bajo_la_curva_parallel.py

normal:
	python3 area_bajo_la_curva.py

compile:
	gcc -fPIC -shared -o area_bajo_la_curva.so area_bajo_la_curva.c

clean:
	rm -rf *.so