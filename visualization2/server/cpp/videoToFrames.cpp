#include <opencv2/opencv.hpp>
#include <opencv2/core/types_c.h>
#include <vector>
#include <string>
#include <ctime>
#include <time.h>
#include <chrono>
#include <algorithm>


using namespace std;
using namespace cv;
using namespace std::chrono;

void splitVideo(const string vidFile, vector<Mat>& frames);
void saveFrames(vector<Mat>& frames, const string& saveDirectory);

int main(){
	vector<Mat> frames;
	auto start  = high_resolution_clock::now();

	splitVideo("../uploads/ExampleVideo.mp4", frames);
	saveFrames(frames, "../dataset/");
	auto stop = high_resolution_clock::now();
	auto duration = duration_cast<seconds>(stop-start);

	cout << "Time taken: " << duration.count() << " seconds" << endl;

	return 0;
}

void splitVideo(const string vidFile, vector<Mat>& frames){
	try{
		VideoCapture cap(vidFile);
		if(!cap.isOpened())
			CV_Error(CV_StsError, "Can't open video file");
		cout << "Number of frames: " << cap.get(CAP_PROP_FRAME_COUNT) << endl;

		for(int frameNum = 0 ; frameNum < cap.get(CAP_PROP_FRAME_COUNT) ; ++frameNum){
			Mat frame;
			cap >> frame;
			frames.push_back(frame);
		}
	}
	catch(Exception& e){
		cerr << e.msg << endl;
		exit(1);
	}
}

void saveFrames(vector<Mat>& frames, const string& saveDirectory){
	vector<int> compression_parameters;
	compression_parameters.push_back(IMWRITE_JPEG_QUALITY);
	compression_parameters.push_back(100);

	int frameNumber = 0;
	for(vector<Mat>::iterator frame = frames.begin() ; frame != frames.end() ; ++frame, ++frameNumber){
		string filePath = saveDirectory + to_string(static_cast<long long>(frameNumber)) + ".jpg";
		imwrite(filePath, *frame, compression_parameters);
	}
}