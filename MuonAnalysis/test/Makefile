all: MakeReducedNtuple_NANO.x makeTrees1.x makeTrees2.x

MakeReducedNtuple_NANO.x: NanoTreeTemplate.o ./MakeReducedNtuple_NANO.C ./NanoTreeTemplate.h
	g++ -o MakeReducedNtuple.x ./MakeReducedNtuple_NANO.C NanoTreeTemplate.o `root-config --cflags --libs`

NanoTreeTemplate.o: ./NanoTreeTemplate.h ./NanoTreeTemplate.C
	g++ -c ./NanoTreeTemplate.C `root-config --cflags --libs`

makeTrees1.x: softLepNANO.o ./makeTrees1.C ./softLepNANO.h
	g++ -o makeTrees1.x ./makeTrees1.C softLepNANO.o `root-config --cflags --libs`

makeTrees2.x: softLepMINI.o ./makeTrees2.C ./softLepMINI.h
	g++ -o makeTrees2.x ./makeTrees2.C softLepMINI.o `root-config --cflags --libs`

softLepMINI.o: ./softLepMINI.h ./softLepMINI.C
	g++ -c ./softLepMINI.C `root-config --cflags --libs`

softLepNANO.o: ./softLepNANO.h ./softLepNANO.C
	g++ -c ./softLepNANO.C `root-config --cflags --libs`

clean:
	rm *.o
	rm -f *.x
