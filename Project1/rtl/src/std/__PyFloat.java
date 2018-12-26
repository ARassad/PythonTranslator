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
public class __PyFloat extends __PyGenericObject {

    public __PyFloat() {
        super();
    }
    
    public __PyFloat(float value) {
        this();
        this.__float__ = value;
    }
    
    public __PyFloat(String value) {
        this();
        this.__float__ = Float.parseFloat(value);
    }
    
    public __PyGenericObject __str__() {
        return new __PyString(Double.toString(this.__float__));
    }
    
    public __PyGenericObject __list__() {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __float__() {
        return this;
    }
    
    public __PyGenericObject __int__() {
        return new __PyInteger((int) this.__float__);
    }
    
    public __PyGenericObject __bool__() {
        return new __PyInteger(this.__float__ != 0.0);
    }
    
    //Arifmetic 
    public __PyGenericObject __abs__() {
        return new __PyFloat(Math.abs(this.__float__));
    }
    
    public __PyGenericObject __add__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ + value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ + value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __sub__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ - value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ - value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __mul__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ * value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ * value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __truediv__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ / value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ / value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __floordiv__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger((int)Math.floor(this.__float__ / value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyInteger((int)Math.floor(this.__float__ / value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __mod__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__float__ % value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__float__ % value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __pow__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyFloat((float)Math.pow(this.__float__, value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyFloat((float)Math.pow(this.__float__ , value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with float must be int or float.");
    }
    
    public __PyGenericObject __neg__() {
        return new __PyFloat(this.__float__ * -1);
    }
    
    public __PyGenericObject __pos__() {
        return this;
    }
    
    public __PyGenericObject __round__() {
        return new __PyFloat(Math.round(this.__float__));
    }
    
    // Equal
    public __PyGenericObject __lt__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ < value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ < value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyGenericObject __le__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ <= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ <= value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyGenericObject __eq__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ == value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ == value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyGenericObject __ne__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ != value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ != value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyGenericObject __gt__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ > value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ > value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
    
    public __PyGenericObject __ge__(__PyGenericObject value) throws NotImplementedException {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__float__ >= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__float__ >= value.__float__);
        
        throw new ArithmeticException("Object for equality with float must be int or float.");
    }
}
