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
public class Str extends basic{
    public String strVal;
    
    @Override
    public Str add(basic other)
    {
        Str result = new Str();
        result.strVal = this.strVal + ((Str)other).strVal;
        return result;
    }
    @Override
    public Str minus(basic other)
    {
        try {
            throw new Exception("cannot use operation minus for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    @Override
    public Str mul(basic other)
    {
        try {
            throw new Exception("cannot use operation mul for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    @Override
    public Str div(basic other)
    {
        try {
            throw new Exception("cannot use operation mul for the type string");
        } catch (Exception ex) {
            Logger.getLogger(Str.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
