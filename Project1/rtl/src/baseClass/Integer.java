/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baseClass;

/**
 *
 * @author 1
 */
public class Integer extends __PyObject {
    public int intVal;
    public Integer __add__(__PyObject other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal + ((Integer)other).intVal;
        return result;

    }
    public Integer __minus__(__PyObject other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal + ((Integer)other).intVal;
        return result;
    }
    public Integer __mul__(__PyObject other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal * ((Integer)other).intVal;
        return result;
    }
    public Integer __div__(__PyObject other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal * ((Integer)other).intVal;
        return result;
    }
    
}
