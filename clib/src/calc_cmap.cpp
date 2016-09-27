#include <Python.h>
#include "/usr/lib/python2.7/dist-packages/numpy/core/include/numpy/arrayobject.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double clength(double x1,double y1,double z1,double x2,double y2,double z2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2));
}
static 
PyObject* ccmap(PyObject *xyz_data,double cut_length)
{
    long i,j;
    long max=PyList_Size(xyz_data);
    PyObject* xyz_item1,*xyz_item2;
    PyObject *out_list,*out_list2;
    out_list=PyList_New(max);
    double nowlength;
    long d2_list[max][max];

    for(i=0;i<max;i++){
        for(j=0;j<max;j++){
            d2_list[j][i]=0;
        }
    }
    
    for(i=0;i<max;i++){
        for(j=i+4;j<max;j++){
            xyz_item1=PyList_GetItem(xyz_data,i);
            xyz_item2=PyList_GetItem(xyz_data,j);
            nowlength=clength(PyFloat_AsDouble(PyList_GetItem(xyz_item1,0)),
                              PyFloat_AsDouble(PyList_GetItem(xyz_item1,1)),
                              PyFloat_AsDouble(PyList_GetItem(xyz_item1,2)),
                              PyFloat_AsDouble(PyList_GetItem(xyz_item2,0)),
                              PyFloat_AsDouble(PyList_GetItem(xyz_item2,1)),
                              PyFloat_AsDouble(PyList_GetItem(xyz_item2,2)));
            if(nowlength<cut_length){
                d2_list[j][i]=1;
            }else{
                d2_list[j][i]=0;
            }
        }
    }

    for(i=0;i<max;i++){
        for(j=i;j<max;j++){
            d2_list[i][j]=d2_list[j][i];
            if(i==j){
                d2_list[i][j]=1;
            }
        }
    }

    for(i=0;i<max;i++){
        out_list2=PyList_New(max);
        for(j=0;j<max;j++){
            PyList_SetItem(out_list2,j,PyInt_FromLong(d2_list[j][i]));
        }
        PyList_SetItem(out_list,i,out_list2);
    }
    return out_list;
}

static PyObject* wrap_ccmap(PyObject* self,PyObject* args)
{
    PyObject *xyz_data;
    double cut_length;
    if(!PyArg_ParseTuple(args,"Od",
                         &xyz_data,
                         &cut_length
                         )){
        return NULL;
    }
    return ccmap(xyz_data,cut_length);
}

static PyMethodDef ccmapmethods[]={
    {"ccmap",wrap_ccmap,METH_VARARGS},
    {NULL},
};

void initccmap()
{
    Py_InitModule("ccmap",ccmapmethods);
    import_array();
}
