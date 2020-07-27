# JAVA-POJO-Generator
An tool made for JAVA POJO genration less then a second.
 eg. sample_xml
https://github.com/keshri23jayesh/JAVA-POJO-Genrator/blob/master/xml_to_pojo/sample.xml

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
