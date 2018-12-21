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
public class __PyFloat extends __PyObject {

    public __PyFloat() {
        super();
    }
    
    public __PyFloat(double value) {
        this();
        this.__float__ = value;
    }
    
    public __PyFloat(String value) {
        this();
        this.__float__ = Double.parseDouble(value);
    }
    
    public __PyObject __str__() {
        return new __PyString(Double.toString(this.__float__));
    }
    
    public __PyObject __list__() {
        throw new NotImplementedException();
    }
    
    public __PyObject __float__() {
        return this;
    }
    
    public __PyObject __int__() {
        return new __PyInteger((int) this.__float__);
    }
    
    public __PyObject __bool__() {
        return new __PyInteger(this.__float__ != 0.0);
    }
    
    //Arifmetic 
    public __PyObject __abs__() {
        return new __PyFloat(Math.abs(this.__float__));
    }
    
    public __PyObject __add__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ + value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ + value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __sub__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ - value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ - value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __mul__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ * value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ * value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __truediv__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ / value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ / value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __floordiv__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger((int)Math.floor(this.__float__ / value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyInteger((int)Math.floor(this.__float__ / value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __mod__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ % value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ % value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __pow__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyFloat(Math.pow(this.__float__, value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyFloat(Math.pow(this.__float__ , value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyObject __neg__() {
        return new __PyFloat(this.__float__ - 1);
    }
    
    public __PyObject __pos__() {
        return new __PyFloat(this.__float__ + 1);
    }
    
    public __PyObject __round__() {
        return new __PyFloat(Math.round(this.__float__));
    }
    
    // Equal
    public __PyObject __lt__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ < value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ < value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyObject __le__(__PyObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ <= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ <= value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyObject __eq__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ == value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ == value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyObject __ne__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ != value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ != value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyObject __gt__(__PyObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ > value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ > value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyObject __ge__(__PyObject value) throws NotImplementedException {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ >= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ >= value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
}
