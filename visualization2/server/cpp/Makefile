#compiler
CC = g++
#the build target executable
#TARGET = videoToFrames
CFLAGS = 
LIBS = -L/usr/local/lib -lcppunit -ldl -lopencv_core -lopencv_imgcodecs -lopencv_videoio -lopencv_imgproc

all:
		sudo $(CC) $(CFLAGS) -I -o videoToFrames.cpp $(LIBS)

clean:
	@sudo rm -rf ./a.out