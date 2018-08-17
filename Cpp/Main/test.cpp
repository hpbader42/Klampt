#include "Interface/RobotTestGUI.h"

int main(int argc,const char** argv)
{
  RobotWorld world;
  RobotTestBackend backend(&world);
  if(!backend.LoadCommandLine(argc,argv)) {
    return 1;
  }
#if HAVE_GLUI
  GLUIRobotTestGUI gui(&backend,&world);
  gui.SetWindowTitle("RobotTest");
  gui.Run();
  return 0;
#endif //HAVE_GLUI
}
