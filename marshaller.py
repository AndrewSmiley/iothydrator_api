# package com.ge.predix.entity.timeseries.datapoints.ingestionrequest;
#
# import com.ge.predix.entity.fielddata.Data;
# import java.io.Serializable;
# import java.util.ArrayList;
# import java.util.List;
# import javax.xml.bind.annotation.XmlAccessType;
# import javax.xml.bind.annotation.XmlAccessorType;
# import javax.xml.bind.annotation.XmlElement;
# import javax.xml.bind.annotation.XmlRootElement;
# import javax.xml.bind.annotation.XmlType;
# import org.jvnet.jaxb2_commons.lang.Equals;
# import org.jvnet.jaxb2_commons.lang.EqualsStrategy;
# import org.jvnet.jaxb2_commons.lang.HashCode;
# import org.jvnet.jaxb2_commons.lang.HashCodeStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBEqualsStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBHashCodeStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBToStringStrategy;
# import org.jvnet.jaxb2_commons.lang.ToString;
# import org.jvnet.jaxb2_commons.lang.ToStringStrategy;
# import org.jvnet.jaxb2_commons.locator.ObjectLocator;
# import org.jvnet.jaxb2_commons.locator.util.LocatorUtils;
#
# @XmlAccessorType(XmlAccessType.FIELD)
# @XmlType(name="", propOrder={"messageId", "body"})
# @XmlRootElement(name="DatapointsIngestion")
# public class DatapointsIngestion
#   extends Data
#   implements Serializable, Equals, HashCode, ToString
# {
#   @XmlElement(required=true)
#   protected String messageId;
#   protected List<Body> body;
#
#   public String getMessageId()
#   {
#     return this.messageId;
#   }
#
#   public void setMessageId(String value)
#   {
#     this.messageId = value;
#   }
#
#   public List<Body> getBody()
#   {
#     if (this.body == null) {
#       this.body = new ArrayList();
#     }
#     return this.body;
#   }
#
#   public void setBody(List<Body> body)
#   {
#     this.body = body;
#   }
#
#   public String toString()
#   {
#     ToStringStrategy strategy = JAXBToStringStrategy.INSTANCE;
#     StringBuilder buffer = new StringBuilder();
#     append(null, buffer, strategy);
#     return buffer.toString();
#   }
#
#   public StringBuilder append(ObjectLocator locator, StringBuilder buffer, ToStringStrategy strategy)
#   {
#     strategy.appendStart(locator, this, buffer);
#     appendFields(locator, buffer, strategy);
#     strategy.appendEnd(locator, this, buffer);
#     return buffer;
#   }
#
#   public StringBuilder appendFields(ObjectLocator locator, StringBuilder buffer, ToStringStrategy strategy)
#   {
#     super.appendFields(locator, buffer, strategy);
#
#     String theMessageId = getMessageId();
#     strategy.appendField(locator, this, "messageId", buffer, theMessageId);
#
#     List<Body> theBody = (this.body != null) && (!this.body.isEmpty()) ? getBody() : null;
#     strategy.appendField(locator, this, "body", buffer, theBody);
#
#     return buffer;
#   }
#
#   public boolean equals(ObjectLocator thisLocator, ObjectLocator thatLocator, Object object, EqualsStrategy strategy)
#   {
#     if (!(object instanceof DatapointsIngestion)) {
#       return false;
#     }
#     if (this == object) {
#       return true;
#     }
#     if (!super.equals(thisLocator, thatLocator, object, strategy)) {
#       return false;
#     }
#     DatapointsIngestion that = (DatapointsIngestion)object;
#
#     String lhsMessageId = getMessageId();
#
#     String rhsMessageId = that.getMessageId();
#     if (!strategy.equals(LocatorUtils.property(thisLocator, "messageId", lhsMessageId), LocatorUtils.property(thatLocator, "messageId", rhsMessageId), lhsMessageId, rhsMessageId)) {
#       return false;
#     }
#     List<Body> lhsBody = (this.body != null) && (!this.body.isEmpty()) ? getBody() : null;
#
#     List<Body> rhsBody = (that.body != null) && (!that.body.isEmpty()) ? that.getBody() : null;
#     if (!strategy.equals(LocatorUtils.property(thisLocator, "body", lhsBody), LocatorUtils.property(thatLocator, "body", rhsBody), lhsBody, rhsBody)) {
#       return false;
#     }
#     return true;
#   }
#
#   public boolean equals(Object object)
#   {
#     EqualsStrategy strategy = JAXBEqualsStrategy.INSTANCE;
#     return equals(null, null, object, strategy);
#   }
#
#   public int hashCode(ObjectLocator locator, HashCodeStrategy strategy)
#   {
#     int currentHashCode = super.hashCode(locator, strategy);
#
#     String theMessageId = getMessageId();
#     currentHashCode = strategy.hashCode(LocatorUtils.property(locator, "messageId", theMessageId), currentHashCode, theMessageId);
#
#     List<Body> theBody = (this.body != null) && (!this.body.isEmpty()) ? getBody() : null;
#     currentHashCode = strategy.hashCode(LocatorUtils.property(locator, "body", theBody), currentHashCode, theBody);
#
#     return currentHashCode;
#   }
#
#   public int hashCode()
#   {
#     HashCodeStrategy strategy = JAXBHashCodeStrategy.INSTANCE;
#     return hashCode(null, strategy);
#   }
# }
#
#
#
#
# class DatapointsIngestion():
#     def __int__(self):
#         self.messageId = None
#         self.body = []
# package com.ge.predix.entity.fielddata;
#
# import com.fasterxml.jackson.annotation.JsonTypeInfo;
# import com.fasterxml.jackson.annotation.JsonTypeInfo.As;
# import com.fasterxml.jackson.annotation.JsonTypeInfo.Id;
# import com.ge.predix.entity.asset.AssetList;
# import com.ge.predix.entity.datafile.DataFile;
# import com.ge.predix.entity.metadata.MetaData;
# import com.ge.predix.entity.metadata.MetaDataList;
# import com.ge.predix.entity.model.Model;
# import com.ge.predix.entity.model.ModelList;
# import com.ge.predix.entity.timeseries.aggregations.AggregationsList;
# import com.ge.predix.entity.timeseries.datapoints.ingestionrequest.DatapointsIngestion;
# import com.ge.predix.entity.timeseries.datapoints.queryresponse.DatapointsResponse;
# import com.ge.predix.entity.timeseries.tags.TagsList;
# import com.ge.predix.entity.util.map.DataMap;
# import java.io.Serializable;
# import javax.xml.bind.annotation.XmlAccessType;
# import javax.xml.bind.annotation.XmlAccessorType;
# import javax.xml.bind.annotation.XmlSeeAlso;
# import javax.xml.bind.annotation.XmlType;
# import org.jvnet.jaxb2_commons.lang.Equals;
# import org.jvnet.jaxb2_commons.lang.EqualsStrategy;
# import org.jvnet.jaxb2_commons.lang.HashCode;
# import org.jvnet.jaxb2_commons.lang.HashCodeStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBEqualsStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBHashCodeStrategy;
# import org.jvnet.jaxb2_commons.lang.JAXBToStringStrategy;
# import org.jvnet.jaxb2_commons.lang.ToString;
# import org.jvnet.jaxb2_commons.lang.ToStringStrategy;
# import org.jvnet.jaxb2_commons.locator.ObjectLocator;
#
# @XmlAccessorType(XmlAccessType.FIELD)
# @XmlType(name="Data")
# @XmlSeeAlso({DataMap.class, PredixDate.class, OsaData.class, PredixFloat.class, PredixHexBinary.class, PredixString.class, PredixBoolean.class, PredixDouble.class, Fields.class, PredixDateTime.class, PredixDecimal.class, PredixInt.class, PredixTime.class, AssetList.class, ModelList.class, MetaData.class, MetaDataList.class, Model.class, DataFile.class, DatapointsResponse.class, TagsList.class, DatapointsIngestion.class, AggregationsList.class})
# @JsonTypeInfo(include=JsonTypeInfo.As.PROPERTY, use=JsonTypeInfo.Id.NAME, property="complexType")
# public class Data
#   implements Serializable, Equals, HashCode, ToString
# {
#   public String toString()
#   {
#     ToStringStrategy strategy = JAXBToStringStrategy.INSTANCE;
#     StringBuilder buffer = new StringBuilder();
#     append(null, buffer, strategy);
#     return buffer.toString();
#   }
#
#   public StringBuilder append(ObjectLocator locator, StringBuilder buffer, ToStringStrategy strategy)
#   {
#     strategy.appendStart(locator, this, buffer);
#     appendFields(locator, buffer, strategy);
#     strategy.appendEnd(locator, this, buffer);
#     return buffer;
#   }
#
#   public StringBuilder appendFields(ObjectLocator locator, StringBuilder buffer, ToStringStrategy strategy)
#   {
#     return buffer;
#   }
#
#   public boolean equals(ObjectLocator thisLocator, ObjectLocator thatLocator, Object object, EqualsStrategy strategy)
#   {
#     if (!(object instanceof Data)) {
#       return false;
#     }
#     if (this == object) {
#       return true;
#     }
#     return true;
#   }
#
#   public boolean equals(Object object)
#   {
#     EqualsStrategy strategy = JAXBEqualsStrategy.INSTANCE;
#     return equals(null, null, object, strategy);
#   }
#
#   public int hashCode(ObjectLocator locator, HashCodeStrategy strategy)
#   {
#     int currentHashCode = 1;
#     return currentHashCode;
#   }
#
#   public int hashCode()
#   {
#     HashCodeStrategy strategy = JAXBHashCodeStrategy.INSTANCE;
#     return hashCode(null, strategy);
#   }
# }


# {
#    "messageId": "<MessageID>",
#    "body":[
#       {
#          "name":"<TagName>",
#          "datapoints":[
#             [
#                <EpochInMs>,
#                <Measure>,
#                <Quality>
#             ]
#          ],
#          "attributes":{
#             "<AttributeKey>":"<AttributeValue>",
#             "<AttributeKey2>":"<AttributeValue2>"
#          }
#       }
#    ]
# }
import json

class Datapoint:
    def __init__(self, **kwargs):
        # time=None, measure=None, quality=None
        self.time = kwargs.get("time", None)
        self.measure = kwargs.get("measure", None)
        self.quality = kwargs.get("quality", None)

    def validate(self):
        if not isinstance(self.time, int):
            print "Time is not a valid unix timestamp"
            raise  AssertionError

        if not isinstance(self.measure, float):
            if not isinstance(self.measure, int):
                print "Measure is not numeric"
                raise AssertionError

        if self.quality not in [x for x in range(0,4)]:
            print "Quality is not a valid integer in options %s" % ([x for x in range(0,4)])
            raise AssertionError

    def jsonify(self):
        return [self.time, self.measure, self.quality]


class Body:
    def __init__(self, **kwargs):
        self.attributes = kwargs.get("attributes", {})
        self.name = kwargs.get("name", None)
        self.datapoints = kwargs.get("datapoints", [])

    def add_attribute(self,k,v):
        self.attributes[k] =v
    def add_datapoint(self, dp):
        if not isinstance(dp, Datapoint):
            print "Cannot add datapoint that is not a Datapoint object"
            raise AssertionError

    def validate(self):
        for dp in self.datapoints:
            dp.validate()

        if self.name is None:
            print "Body name is empty"
            raise  AssertionError
        for k, v in self.attributes:
            if not isinstance(k, str) or not isinstance(v, str):
                print "Attribute %s:%s is not valid" %(k, v)
                raise AssertionError
    def jsonify(self):
        self.validate()
        return {"name":self.name, "datapoints":[x.jsonify() for x in self.datapoints], "attributes":self.attributes}


#fuck predix's lack of data validation. That is all
class DatapointsIngestion():
    def __init__(self, **kwargs):
        # messageId=None, body=[]
        self.messageId = kwargs.get("messageId", None)
        self.body = kwargs.get('body', [])

    def validate(self):
        if self.messageId is None or not isinstance(self.messageId, str):
            print "MessageID %s Invalid"%(self.messageId)
            raise AssertionError

        for b in self.body:
            b.validate()

    def add_entry(self, entry):
        if not isinstance(entry, Body):
            print "Attempting to add an invalid object type to body"
        entry.validate()
        self.body.append(entry)

    def jsonify(self):
        self.validate()
        return {"messageId": self.messageId, "body":[x.jsonify() for x in self.body] }


#ok let's test it
d0 =Datapoint(time=1488592273169, measure=69.1, quality=3)
d1 = Datapoint(time=1488592273168, measure=72.1, quality=3)
datapoints =[d0, d1]
b0 =Body(attributes={"aa":"attribute a", "ab":"attribute b"}, name="dp", datapoints=datapoints)

d = DatapointsIngestion(messageId="m14885922731", body=[b0])
print json.dumps(d.jsonify())


import requests
headers={"authorization": "auth"}
data= {'timestamp'}
r = requests.get("localhost:9092/services/windservices/add_datapoint", )


