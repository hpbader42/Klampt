#include "Interface/SimTestGUI.h"
#include <stdio.h>

#if HAVE_GLUI

int main(int argc,const char** argv)
{
  RobotWorld world;
  SimTestBackend backend(&world);
  if(!backend.LoadAndInitSim(argc,argv)) {
    return 1;
  }
  GLUISimTestGUI gui(&backend,&world);
  gui.SetWindowTitle("SimTest");
  gui.Run();
  return 0;
}

#endif // HAVE_GLUI