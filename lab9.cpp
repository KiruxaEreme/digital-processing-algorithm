#include <iostream>
#include <time.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main( int argc, char** argv ) {
    const string url = "http://192.168.15.239:8080/video";
    VideoCapture cap;
    int ret;
    ret = cap.set(3, 320);
    ret = cap.set(4, 240);
    if (!cap.open(url)) 
    {
        cout << "Cannot open the web cam" << endl;
        return -1;
    }

    int iLowH = 170;
    int iHighH = 179;
    int iLowS = 150;
    int iHighS = 255;
    int iLowV = 60;
    int iHighV = 255;

    int iLastX = -1;
    int iLastY = -1;

    int frames = 0;
    while (true) {
        Mat imgOriginal;
        bool bSuccess = cap.read(imgOriginal); 
        if (!bSuccess) {
            cout << "Cannot read a frame from video stream" << endl;
            break;
        }


        Mat imgHSV;
        cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV); 
        Mat imgThresholded;
        inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgThresholded); 

        erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        
        dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));

        Moments oMoments = moments(imgThresholded);
        double dM01 = oMoments.m01;
        double dM10 = oMoments.m10;
        double dArea = oMoments.m00;

        if (dArea > 10000)
        {
            int posX = dM10 / dArea;
            int posY = dM01 / dArea;
            if (iLastX >= 0 && iLastY >= 0 && posX >= 0 && posY >= 0)
            {
                rectangle(imgOriginal, Point(posX-80, posY+80), Point(posX+80, posY-80), Scalar(0,0,0), -1);
            }
            iLastX = posX;
            iLastY = posY;
        }
        resizeWindow("Thresholded Image", 1280, 800);
        imshow("Thresholded Image", imgThresholded); 

        resizeWindow("Original", 1280, 800);
        imshow("Original", imgOriginal);

        if (waitKey(30) == 27)
        {
            cout << "esc key is pressed by user" << endl;
            break;
        }
        frames++;
    }
    
    return 0;
}

// g++ lab9.cpp -o lab9 `pkg-config --cflags --libs opencv4`
// ./lab9