/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;
import java.util.HashMap;
import javax.management.AttributeNotFoundException;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 *
 * @author Arkadi
 */
public abstract class __PyObject {
    public final HashMap<String, __PyObject> __dir__;
    public String __string__;
    public int __integer__;
    
    public __PyObject() {
        this.__dir__ = new HashMap();
    }
    
    //General
    public __PyObject __init__() {
        return null;
    }
    
    public __PyObject __delattr__(String name) {
        throw new NotImplementedException();
    }
    
    public __PyObject __getattr__(String name) throws AttributeNotFoundException {
        __PyObject value = __dir__.get(name);
        if(value == null)
            throw new AttributeNotFoundException("Object has no attribute " + name);
        return value;
    }
    
    public __PyObject __hasattr__(String name) {
        throw new NotImplementedException();
    }
    
    public __PyObject __setattr__(String name, __PyObject value) {
        __dir__.put(name, value);
        return this;
    }
    
    //Method
    public __PyObject __call__() throws Exception {
        throw new Exception("Object is not callable.");
    }
    
    //Type cast
    public __PyObject __str__() throws Exception{
        throw new Exception("Cannot convert object to string.");
    }
    
    public __PyObject __list__() throws Exception{
        throw new Exception("Cannot convert object to list.");
    }
    
    public __PyObject __float__() throws Exception{
        throw new Exception("Cannot convert object to float.");
    }
    
    public __PyObject __int__() throws Exception{
        throw new Exception("Cannot convert object to int.");
    }
    
    public __PyObject __bool__() throws Exception{
        throw new Exception("Cannot convert object to bool.");
    }
    
    // List 
    public __PyObject __contains__(__PyObject value) throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject __delitem__(__PyObject value) throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject __getitem__(__PyObject value) throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject append(__PyObject value) throws NotImplementedException{
        throw new NotImplementedException();
    }
 
    public __PyObject remove(__PyObject value) throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject clear() throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject sort() throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    //Arifmetic 
    public __PyObject __abs__() throws NotImplementedException{
        throw new NotImplementedException();
    }
    
    public __PyObject __add__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __sub__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __mul__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __truediv__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __floordiv__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __mod__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __pow__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __neg__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __pos__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
    }
    
    public __PyObject __round__(__PyObject value) throws NotImplementedException {
        throw new NotImplementedException();
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
