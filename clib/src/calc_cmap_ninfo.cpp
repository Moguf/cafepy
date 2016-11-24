#include <Python.h>
#include "/usr/lib/python2.7/dist-packages/numpy/core/include/numpy/arrayobject.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double clength(double x1,double y1,double z1,double x2,double y2,double z2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2));
}
static
PyObject* ccmapninfo(PyObject *xyz_data,PyObject *ninfo_data)
{
  int i,j;
  PyObject *xyz_item1,*xyz_item2,*ninfo_item,*out_list,*out_list2;
  long ninfo_max=PyList_Size(ninfo_data);
    
  long icon,jcon;
  double nlength;
  double nowcontact=0.0,nowlength=0.0;
  long max=PyList_Size(xyz_data);
  out_list=PyList_New(max);
  long d2_list[max][max];
    
  for(i=0;i<max;i++){
    for(j=0;j<max;j++){
      d2_list[j][i]=0;
    }
  }
  for(i=0;i<ninfo_max;i++){
    ninfo_item=PyList_GetItem(ninfo_data,i);
    icon=PyInt_AsLong(PyList_GetItem(ninfo_item,0));
    jcon=PyInt_AsLong(PyList_GetItem(ninfo_item,1));
    nlength=PyFloat_AsDouble(PyList_GetItem(ninfo_item,2));
    xyz_item1=PyList_GetItem(xyz_data,icon-1);
    xyz_item2=PyList_GetItem(xyz_data,jcon-1);
    nowlength=clength(PyFloat_AsDouble(PyList_GetItem(xyz_item1,0)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item1,1)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item1,2)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,0)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,1)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,2)));
    if(nowlength<nlength*1.2){
      d2_list[icon-1][jcon-1]=1;
      d2_list[jcon-1][icon-1]=1;
    }
  }
  for(i=0;i<max;i++){
    out_list2=PyList_New(max);
    for(j=0;j<max;j++){
      PyList_SetItem(out_list2,j,PyInt_FromLong(d2_list[i][j]));
    }
    PyList_SetItem(out_list,i,out_list2);
  }

  return out_list;
}
PyObject* cnumninfo(PyObject *xyz_data,PyObject *ninfo_data)
{
  int i,j;
  PyObject *xyz_item1,*xyz_item2,*ninfo_item,*out_list,*out_list2;
  long ninfo_max=PyList_Size(ninfo_data);
    
  long icon,jcon;
  double nlength;
  double nowcontact=0.0,nowlength=0.0;
  long max=PyList_Size(xyz_data);
  out_list=PyList_New(max);
  long d2_list[max][max];
    
  for(i=0;i<max;i++){
    for(j=0;j<max;j++){
      d2_list[j][i]=0;
    }
  }
  for(i=0;i<ninfo_max;i++){
    ninfo_item=PyList_GetItem(ninfo_data,i);
    icon=PyInt_AsLong(PyList_GetItem(ninfo_item,0));
    jcon=PyInt_AsLong(PyList_GetItem(ninfo_item,1));
    nlength=PyFloat_AsDouble(PyList_GetItem(ninfo_item,2));
    xyz_item1=PyList_GetItem(xyz_data,icon-1);
    xyz_item2=PyList_GetItem(xyz_data,jcon-1);
    nowlength=clength(PyFloat_AsDouble(PyList_GetItem(xyz_item1,0)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item1,1)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item1,2)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,0)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,1)),
                      PyFloat_AsDouble(PyList_GetItem(xyz_item2,2)));
    if(nowlength<nlength*1.2){
      d2_list[icon-1][jcon-1]=1;
      d2_list[jcon-1][icon-1]=1;
    }
  }
  for(i=0;i<max;i++){
    out_list2=PyList_New(max);
    for(j=0;j<max;j++){
      PyList_SetItem(out_list2,j,PyInt_FromLong(d2_list[i][j]));
    }
    PyList_SetItem(out_list,i,out_list2);
  }

  return out_list;
}




static PyObject* wrap_ccmapninfo(PyObject* self,PyObject* args)
{
  PyObject *xyz_data;
  PyObject *ninfo_data;
  double ans;
  if(!PyArg_ParseTuple(args,"OO",
                       &xyz_data,
                       &ninfo_data
                       )){
    return NULL;
  }
  return ccmapninfo(xyz_data,ninfo_data);
}

static PyMethodDef ccmapninfomethods[]={
  {"ccmapninfo",wrap_ccmapninfo,METH_VARARGS},
  {NULL},
};

void initccmapninfo()
{
  Py_InitModule("ccmapninfo",ccmapninfomethods);
  import_array();
}
