# JAVA-POJO-Genrator
An tool made for JAVA POJO genration less then a second.
 eg. sample_xml
<?xml version="1.0"?>
<data name="Austria" direction="E">
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

Sample base classes by Python APP
public static class rank { 

	private String rank;

	@XmlValue
	public String getrank() {
	return rank;
	}

	public void setrank(String rank) {
	this.rank = rank;
	}

}


public static class year { 

	private String year;

	@XmlValue
	public String getyear() {
	return year;
	}

	public void setyear(String year) {
	this.year = year;
	}

}


public static class gdppc { 

	private String gdppc;

	@XmlValue
	public String getgdppc() {
	return gdppc;
	}

	public void setgdppc(String gdppc) {
	this.gdppc = gdppc;
	}

}


public static class neighbor { 

	private String name;
	private String direction;

	@XmlValue
	public String getneighbor() {
	return neighbor;
	}

	public void setneighbor(String neighbor) {
	this.neighbor = neighbor;
	}

	@XmlAttribute(name="name")
	public String getname() {
	return name;
	}

	public void setname(String name) {
	this.name = name;
	}

	@XmlAttribute(name="direction")
	public String getdirection() {
	return direction;
	}

	public void setdirection(String direction) {
	this.direction = direction;
	}

}
