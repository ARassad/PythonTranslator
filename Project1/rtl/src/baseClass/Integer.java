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
public class Integer extends basic {
    public int intVal;
    @Override
    public Integer add(basic other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal + ((Integer)other).intVal;
        return result;

    }
    @Override
    public Integer minus(basic other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal + ((Integer)other).intVal;
        return result;
    }
    @Override
    public Integer mul(basic other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal * ((Integer)other).intVal;
        return result;
    }
    @Override
    public Integer div(basic other)
    {
        Integer result = new Integer();
        result.intVal = this.intVal * ((Integer)other).intVal;
        return result;
    }
}
