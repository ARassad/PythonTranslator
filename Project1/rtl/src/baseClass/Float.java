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
public class Float extends basic {
    public float floatVal;
    @Override
    public Float add(basic other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal + ((Float)other).floatVal;
        return result;

    }
    @Override
    public Float minus(basic other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal - ((Float)other).floatVal;
        return result;
    }
    @Override
    public Float mul(basic other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal * ((Float)other).floatVal;
        return result;
    }
    @Override
    public Float div(basic other)
    {
        Float result = new Float();
        result.floatVal = this.floatVal * ((Float)other).floatVal;
        return result;
    }
}
