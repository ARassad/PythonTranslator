/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.logging.Level;
import java.util.logging.Logger;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 *
 * @author 1
 */
public class __PyString extends __PyObject{

    public __PyString() {
        super();
        __string__ = new String();
    }
    
    public __PyString(String str) {
        this();
        __string__ = str;
    }
    
    public __PyString __add__(__PyObject other) {
        if(!(other instanceof __PyString))
            throw new ArithmeticException("To add to string object must be string.");
                    
        __PyString result = new __PyString();
        result.__string__ = this.__string__ + other.__string__;
        return result;
    }
    
    public __PyString __mul__(__PyObject other){
        if(!(other instanceof __PyInteger))
            throw new ArithmeticException("Can`t multiply string by non int object.");
        
        String strRes = new String(this.__string__);
        for (int i = 1; i < other.__integer__;i++)
            strRes = strRes + this.__string__;
        return new __PyString(strRes);
    }
    
    public __PyObject __lt__(__PyObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return null;
    }
    
   
}
