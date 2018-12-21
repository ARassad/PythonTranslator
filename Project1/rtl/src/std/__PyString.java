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
public class __PyString extends __PyGenericObject{

    public __PyString() {
        super();
        __string__ = new String();
    }
    
    public __PyString(String str) {
        this();
        __string__ = str;
    }
    
    public __PyString __add__(__PyGenericObject other) {
        if(!(other instanceof __PyString))
            throw new ArithmeticException("To add to string object must be string.");
                    
        __PyString result = new __PyString();
        result.__string__ = this.__string__ + other.__string__;
        return result;
    }
    
    public __PyString __mul__(__PyGenericObject other){
        if(!(other instanceof __PyInteger))
            throw new ArithmeticException("Can`t multiply string by non int object.");
        
        String strRes = new String(this.__string__);
        for (int i = 1; i < other.__integer__;i++)
            strRes = strRes + this.__string__;
        return new __PyString(strRes);
    }
    
    public __PyGenericObject __lt__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) < 0);
    }
    
    public __PyGenericObject __le__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) <= 0);
    }
    
    public __PyGenericObject __eq__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) == 0);
    }
    
    public __PyGenericObject __ne__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) != 0);
    }
    
    public __PyGenericObject __gt__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) > 0);
    }
    
    public __PyGenericObject __ge__(__PyGenericObject value) {
        if(!(value instanceof __PyString))
            throw new ArithmeticException("Object for compare must be string.");
        
        return new __PyInteger(this.__string__.compareTo(value.__string__) >= 0);
    }
    
    //Type cast
    public __PyGenericObject __str__(){
        return this;
    }
    
    public __PyGenericObject __list__() {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __float__() {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __int__()  {
        return new __PyInteger(Integer.parseInt(this.__string__));
    }
    
    public __PyGenericObject __bool__() {
        return new __PyInteger(this.__string__.length() != 0);
    }
}
