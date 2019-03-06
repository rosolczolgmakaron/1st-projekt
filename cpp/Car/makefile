CXX=g++
CXXFLAGS=-Wall -I.
OBJS=samochod.o car.o

cel: samochod.o car.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o samochod.exe

.PHONY: clean

clean:
	rm -f *.o *.exe *~ core *~
