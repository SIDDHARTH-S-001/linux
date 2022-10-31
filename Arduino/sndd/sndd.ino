#include "arduinoFFT.h"
 
#define SAMPLES 128
#define SAMPLING_FREQUENCY 2048
 
arduinoFFT FFT = arduinoFFT();
 
unsigned int samplingPeriod;
unsigned long microSeconds;

int threshhold = 750;
int cnt = 0;
int lefts[16];
int lds = 0;
int rights[16];
int rds = 0;
int ldir = 0;
int rdir = 0;
int freql[3];
int freqr[3];

int ml,il,mr,ir;

void lLED(int one,int two,int three){
  
}
void rLED(int one,int two,int three){
  
}
  
void alarm(int left, int right){
  
}


int maxf(int l[],int len){
  int m = 0; 
  int in = 0;
  for (int j = 0;j<len;j++){
    if (m<=l[j]){
      m = l[j];
      in = j;
    }
  }
  return m,in;
}

int mfreq(int rdat){
  double vReal[SAMPLES];
  double vImag[SAMPLES];
  for(int i=0; i<SAMPLES; i++)
    {
        microSeconds = micros();   
     
        vReal[i] = rdat;
        vImag[i] = 0; 

        while(micros() < (microSeconds + samplingPeriod)){}
    }
 
    FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
    FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);

    double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQUENCY);
    return (peak);

}


 
void setup() 
{
    Serial.begin(115200);
    samplingPeriod = round(1000000*(1.0/SAMPLING_FREQUENCY));
}
 
void loop(){
   
for(int i = 0;i<16;i++){  
   int x = analogRead(A0);
   freql[0] = mfreq(x);
   x = analogRead(A1);
   freql[1] = mfreq(x);
   x = analogRead(A2);
   freql[2] = mfreq(x);
   x = analogRead(A3);
   freqr[0] = mfreq(x);
   x = analogRead(A4);
   freqr[1] = mfreq(x);
   x = analogRead(A5);
   freqr[2] = mfreq(x);
   
   ml,il = maxf(freql,3);
   mr,ir = maxf(freqr,3);
if (ml>threshhold){
  alarm(1,0);
}
else if (mr>threshhold){
  alarm(0,1);
}
    else{
      lds+=il;
      rds+=ir;
      cnt+=1;
      if(cnt == 16){
        cnt = 0;
        ldir = round(lds/16);
        rdir = round(rds/16);
        lds = 0;
        rds = 0;
        if (ldir == 1){
          lLED(1,0,0);
        }
        else if(ldir == 2){
          lLED(0,1,0);
        }
        else if(ldir == 3){
          lLED(0,0,1);
        }
        if (rdir == 1){
          rLED(1,0,0);
        }
        else if(rdir == 2){
          rLED(0,1,0);
        }
        else if(rdir == 3){
          rLED(0,0,1);
        }
      }
    }
    
   delay(20);
}
}
