/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import sun.reflect.generics.reflectiveObjects.NotImplementedException;
/**
 *
 * @author 1
 */
public class __PyInteger extends __PyObject {

    public __PyInteger() {
        super();
    }
    
    public __PyInteger(boolean value) {
        this();
        this.__integer__ = 0;
        if(value)
            this.__integer__ = 1;
    }
    
    public __PyInteger(int value) {
        this();
        this.__integer__ = value;
    }
    
    public __PyInteger(String value) {
        this();
        this.__integer__ = Integer.parseInt(value);
    }
    
    public __PyObject __str__() {
        return new __PyString(Integer.toString(this.__integer__));
    }
    
    public __PyObject __list__() {
        throw new NotImplementedException();
    }
    
    public __PyObject __float__() {
        throw new NotImplementedException();
    }
    
    public __PyObject __int__() {
        return this;
    }
    
    public __PyObject __bool__() {
        return new __PyInteger(this.__integer__ != 0);
    }
    
    //Arifmetic 
    public __PyObject __abs__() {
        return new __PyInteger(Math.abs(this.__integer__));
    }
    
    public __PyObject __add__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ + value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ + value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __sub__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ - value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ - value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __mul__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ * value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ * value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __truediv__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__integer__ / value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ / value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __floordiv__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger((int)Math.floor(this.__integer__ / value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyInteger((int)Math.floor(this.__integer__ / value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __mod__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__integer__ % value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ % value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __pow__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyFloat(Math.pow(this.__integer__, value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyFloat(Math.pow(this.__integer__ , value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyObject __neg__() {
        return new __PyInteger(this.__integer__ - 1);
    }
    
    public __PyObject __pos__() {
        return new __PyInteger(this.__integer__ + 1);
    }
    
    public __PyObject __round__() throws NotImplementedException {
        return new __PyInteger(Math.round(this.__integer__));
    }
    
    //Logic
    public __PyObject __and__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __or__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __xor__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    // Equal
    public __PyObject __lt__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __le__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __eq__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __ne__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __gt__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __ge__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
}
