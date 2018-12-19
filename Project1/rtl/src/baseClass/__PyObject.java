/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baseClass;
import java.util.HashMap;
import javax.management.AttributeNotFoundException;

/**
 *
 * @author Arkadi
 */
public abstract class __PyObject {
    public final HashMap<String, __PyObject> __dir__;

    public __PyObject() {
        this.__dir__ = new HashMap();
        __init__();
    }
    
    public __PyObject __init__() {
        return null;
    }
    
    public __PyObject __delattr__(String name) {
        return null;
    }
    
    public __PyObject __getattr__(String name) throws AttributeNotFoundException {
        __PyObject value = __dir__.get(name);
        if(value == null)
            throw new AttributeNotFoundException("Object has no attribute " + name);
        return value;
    }
    
    public __PyObject __hasattr__(String name) {
        return null;
    }
    
    public __PyObject __setattr__(String name, __PyObject value) {
        __dir__.put(name, value);
        return this;
    }
    
    public __PyObject __call__() throws Exception {
        throw new Exception("Object is not callable.");
    }
    
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
}
