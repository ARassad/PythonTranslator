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
public class Float extends __PyObject {
    public float floatVal;
    public Float __add__(__PyObject other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal + ((Float)other).floatVal;
        return result;

    }
    public Float __minus__(__PyObject other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal - ((Float)other).floatVal;
        return result;
    }
    
    public Float __mul(__PyObject other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal * ((Float)other).floatVal;
        return result;
    }
    public Float div(__PyObject other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal * ((Float)other).floatVal;
        return result;
    }
}
