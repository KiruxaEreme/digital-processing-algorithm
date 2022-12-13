#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main( int argc, char** argv ) {
  
  Mat image, new_imageHSV;
  image = imread("1236.jpg" , 1);
  
  if(! image.data ) {
      cout <<  "Could not open or find the image" << endl ;
      return -1;
    }
    
  int width = image.cols, height = image.rows;
  cvtColor(image, new_imageHSV, COLOR_BGR2HSV);

  int c = (int)new_imageHSV.at<Vec3b>(height/2,width/2)[0];
  Scalar color;
  if(c >= 0 && c < 30 || c >= 150 && c < 180) 
    color = Scalar(0,0,255);
  else if(c >= 30 && c < 90)
    color = Scalar(0,255,0);
  else if(c >= 90 && c < 150)
    color = Scalar(255,0,0);
  
  int w = 50, h = 300;
  int x = (width-w)/2, y = (height-h)/2;
  rectangle(image, Rect(x, y, w, h), color, -1);
  
  x = (width-h)/2, y = (height-w)/2;
  rectangle(image, Rect(x, y, h, w), color, -1);

  namedWindow( "Display window1", WINDOW_NORMAL);
  resizeWindow("Display window1", (width*((700*100)/height))/100, 700);
  imshow( "Display window1", new_imageHSV);

  namedWindow( "Display window2", WINDOW_NORMAL);
  resizeWindow("Display window2", (width*((700*100)/height))/100, 700);
  imshow( "Display window2", image);
  
  waitKey(0);
  return 0;
}
