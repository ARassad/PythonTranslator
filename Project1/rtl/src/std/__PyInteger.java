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
public class __PyInteger extends __PyGenericObject {

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
    
    public __PyGenericObject __str__() {
        return new __PyString(Integer.toString(this.__integer__));
    }
    
    public __PyGenericObject __list__() {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __float__() {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __int__() {
        return this;
    }
    
    public __PyGenericObject __bool__() {
        return new __PyInteger(this.__integer__ != 0);
    }
    
    //Arifmetic 
    public __PyGenericObject __abs__() {
        return new __PyInteger(Math.abs(this.__integer__));
    }
    
    public __PyGenericObject __add__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ + value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ + value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __sub__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ - value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ - value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __mul__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ * value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ * value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __truediv__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__integer__ / value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ / value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __floordiv__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger((int)Math.floor(this.__integer__ / value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyInteger((int)Math.floor(this.__integer__ / value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __mod__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyFloat(this.__integer__ % value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyFloat(this.__integer__ % value.__float__);
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __pow__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyFloat(Math.pow(this.__integer__, value.__integer__));
        else if (value instanceof __PyFloat)
            return new __PyFloat(Math.pow(this.__integer__ , value.__float__));
        
        throw new ArithmeticException("Object for arifmetic with int must be int or float.");
    }
    
    public __PyGenericObject __neg__() {
        return new __PyInteger(this.__integer__ - 1);
    }
    
    public __PyGenericObject __pos__() {
        return new __PyInteger(this.__integer__ + 1);
    }
    
    public __PyGenericObject __round__() {
        return new __PyInteger(Math.round(this.__integer__));
    }
    
    // Equal
    public __PyGenericObject __lt__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ < value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ < value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
    
    public __PyGenericObject __le__(__PyGenericObject value) {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ <= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ <= value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
    
    public __PyGenericObject __eq__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ == value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ == value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
    
    public __PyGenericObject __ne__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ != value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ != value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
    
    public __PyGenericObject __gt__(__PyGenericObject value)  {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ > value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ > value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
    
    public __PyGenericObject __ge__(__PyGenericObject value) throws NotImplementedException {
        if(value instanceof __PyInteger)
            return new __PyInteger(this.__integer__ >= value.__integer__);
        else if (value instanceof __PyFloat)
            return new __PyInteger(this.__integer__ >= value.__float__);
        
        throw new ArithmeticException("Object for equality with int must be int or float.");
    }
}
