#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    Mat image;
    const string url = "http://10.240.99.136:8080/video";
    VideoCapture cap;

    VideoWriter writer;
    int codec = VideoWriter::fourcc('M', 'J', 'P', 'G');
    double fps = 25.0;
    string filename = "./video.avi";
    
    if (!cap.open(url)) {
        cout << "Error! Unable to open camera\n";
        return -1;
    }

    writer.open(filename, codec, fps, Size(1920,1080));
    if (!writer.isOpened()) {
        cout << "Could not open the output video file for write\n";
        return -1;
    }

    namedWindow("Output Window");
    for(;;) {
        if(!cap.read(image)) {
            cout << "No frame" << endl;
            waitKey();
        }
        writer.write(image);
        imshow("Output Window", image);
        if(waitKey(1) >= 0) break;
    } 
    return 0;
}

// g++ record_video.cpp -o record_video `pkg-config --cflags --libs opencv4`
// ./record_video