#include "Python.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double length(double x1,double y1,double z1,double x2,double y2,double z2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2));
}
    
static
double qscore(PyObject *xyz_data,PyObject *ninfo_data)
{
    int i;
	PyObject *xyz_item1,*xyz_item2,*ninfo_item;
    long icon,jcon;
    double nlength;
	double max=PyList_Size(ninfo_data);
    double nowcontact=0.0,nowlength=0.0;

    for(i=0;i<max;i++){
        ninfo_item=PyList_GetItem(ninfo_data,i);
        icon=PyLong_AsLong(PyList_GetItem(ninfo_item,0));
        jcon=PyLong_AsLong(PyList_GetItem(ninfo_item,1));
        nlength=PyFloat_AsDouble(PyList_GetItem(ninfo_item,2));

        xyz_item1=PyList_GetItem(xyz_data,icon-1);
        xyz_item2=PyList_GetItem(xyz_data,jcon-1);
        nowlength=length(PyFloat_AsDouble(PyList_GetItem(xyz_item1,0)),
                          PyFloat_AsDouble(PyList_GetItem(xyz_item1,1)),
                          PyFloat_AsDouble(PyList_GetItem(xyz_item1,2)),
                          PyFloat_AsDouble(PyList_GetItem(xyz_item2,0)),
                          PyFloat_AsDouble(PyList_GetItem(xyz_item2,1)),
                          PyFloat_AsDouble(PyList_GetItem(xyz_item2,2)));
        if(nowlength<nlength*1.2){
            nowcontact+=1;
        }
    }
    return nowcontact/max;
}

static PyObject* wrap_qscore(PyObject* self,PyObject* args)
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
    ans=qscore(xyz_data,ninfo_data);
    return PyFloat_FromDouble(ans);
}

static PyMethodDef qscore_methods[]={
    {"qscore",(PyCFunction)wrap_qscore, METH_VARARGS, NULL},
    {NULL},
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "qscore",
    NULL,
    NULL,
    qscore_methods,
    NULL,
    NULL,
    NULL,
    NULL,
};
    
    

PyMODINIT_FUNC
PyInit_qscore(void){
    PyObject *module = PyModule_Create(&moduledef);

    return module;
}
