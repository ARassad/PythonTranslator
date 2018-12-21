/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.HashMap;
import java.util.LinkedList;
import javax.management.AttributeNotFoundException;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 *
 * @author Arkadi
 */
public abstract class __PyObject {
    public final HashMap<String, __PyGenericObject> __dir__;
    public String __string__;
    public int __integer__;
    public double __float__;
    public LinkedList<__PyGenericObject> __list__;
    
    public __PyObject() {
        this.__dir__ = new HashMap();
    }
    
    //General
    public __PyGenericObject __init__() throws Exception {
        return null;
    }
    
    public __PyGenericObject __delattr__(String name)throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __getattr__(String name) throws Exception {
        __PyGenericObject value = __dir__.get(name);
        if(value == null)
            throw new AttributeNotFoundException("Object has no attribute " + name);
        return value;
    }
    
    public __PyGenericObject __hasattr__(String name) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __setattr__(String name, __PyGenericObject value) throws Exception {
        __dir__.put(name, value);
        return (__PyGenericObject) this;
    }
    
    //Method
    public __PyGenericObject __call__() throws Exception {
        throw new Exception("Object is not callable.");
    }
    
    //Type cast
    public __PyGenericObject __str__() throws Exception{
        throw new Exception("Cannot convert object to string.");
    }
    
    public __PyGenericObject __list__() throws Exception{
        throw new Exception("Cannot convert object to list.");
    }
    
    public __PyGenericObject __float__() throws Exception{
        throw new Exception("Cannot convert object to float.");
    }
    
    public __PyGenericObject __int__() throws Exception{
        throw new Exception("Cannot convert object to int.");
    }
    
    public __PyGenericObject __bool__() throws Exception{
        throw new Exception("Cannot convert object to bool.");
    }
    
    // List 
    public __PyGenericObject __len__() throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __contains__(__PyGenericObject value) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __delitem__(__PyGenericObject index) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __getitem__(__PyGenericObject index) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject append(__PyGenericObject value) throws Exception{
        throw new NotImplementedException();
    }
 
    public __PyGenericObject remove(__PyGenericObject value) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject extend(__PyGenericObject list) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __replaceitem(__PyGenericObject index, __PyGenericObject value) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject insert(__PyGenericObject index, __PyGenericObject value) throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject clear() throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject sort() throws Exception{
        throw new NotImplementedException();
    }
    
    //Arifmetic 
    public __PyGenericObject __abs__() throws Exception{
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __add__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __sub__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __mul__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __truediv__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __floordiv__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __mod__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __pow__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __neg__() throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __pos__() throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __round__() throws Exception {
        throw new NotImplementedException();
    }
    
    //Logic
    public __PyGenericObject __and__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __or__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __xor__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    // Equal
    public __PyGenericObject __lt__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __le__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __eq__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __ne__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __gt__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
    
    public __PyGenericObject __ge__(__PyGenericObject value) throws Exception {
        throw new NotImplementedException();
    }
}
