/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baseClass;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author 1
 */
public class Str extends __PyObject{
    public String strVal;
    
    public Str __add__(__PyObject other)
    {
        Str result = new Str();
        result.strVal = this.strVal + ((Str)other).strVal;
        return result;
    }
    public Str __minus__(__PyObject other)
    {
        try {
            throw new Exception("cannot use operation minus for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    public Str __mul__(__PyObject other)
    {
        try {
            throw new Exception("cannot use operation mul for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    public Str __div__(__PyObject other)
    {
        try {
            throw new Exception("cannot use operation mul for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
