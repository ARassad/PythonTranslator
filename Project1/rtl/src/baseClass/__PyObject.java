/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baseClass;
import java.util.HashMap;

/**
 *
 * @author Arkadi
 */
public abstract class __PyObject {
    public final HashMap<String, __PyObject> __dir__;

    public __PyObject() {
        this.__dir__ = new HashMap();
    }
    
    
    public __PyObject __init__() {
        return null;
    }
    
    public __PyObject __call__() {
        return null;
    }
    
    public __PyObject __delattr__(String name) {
        return null;
    }
    
    public __PyObject __getattr__(String name) {
        return null;
    }
    
    public __PyObject __hasattr__(String name) {
        return null;
    }
    
    public __PyObject __setattr__(String name, __PyObject value) {
        return null;
    }
    
    public abstract __PyObject __str__();
    public abstract __PyObject __list__();
    public abstract __PyObject __float__();
    public abstract __PyObject __int__();
}
