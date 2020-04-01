main: 
NanoTreeTemplate.o ./MakeReducedNtuple_NANO.C ./NanoTreeTemplate.h
	g++ -o MakeReducedNtuple.x ./MakeReducedNtuple_NANO.C NanoTreeTemplate.o `root-config --cflags --libs`
makeTrees.o ./makeTrees.C
	g++ -o makeTrees.x ./makeTrees.C

NanoTreeTemplate.o: ./NanoTreeTemplate.h ./NanoTreeTemplate.C
	g++ -c ./NanoTreeTemplate.C `root-config --cflags --libs`

makeTrees.o: ./makeTrees.C
	g++ -c ./makeTrees.C `root-config --cflags --libs`


clean:
	rm *.o
	rm -f *.x
