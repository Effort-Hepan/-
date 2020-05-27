package cn.hp.Liquor_culture.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Sqlhander {
	private String DBDriver = "com.mysql.jdbc.Driver";
	private String url = "jdbc:mysql://148.70.53.199:3306/Liquor_culture";
	private String id = "root";
	private String password = "1981544603";
	public Connection conn = null;
	public ResultSet rs = null;
	PreparedStatement perstat = null;
	public void setDBDriver(String DBDriver) {
		this.DBDriver = DBDriver;
	}
	public String getDBDriver() {
		return DBDriver;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String getUrl() {
		return url;
	}
	public void setId(String id) {
		this.id= id;
	}
	public String getId() {
		return id;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getPassword() {
		return password;
	}
	
	
	//��ѯ�����׶γ����ϵ������������
	public ResultSet check_part(String mysql) throws Exception{
		try {
			Class.forName(DBDriver);
			conn = DriverManager.getConnection(url,id,password);
			perstat = conn.prepareStatement(mysql);
			//perstat.setString(1, user);
			//perstat.setString(2, psd);
			rs = perstat.executeQuery();
			return rs;
		}
		catch(Exception e) {
			e.printStackTrace();
			System.out.println("��ѯ��analysis_phase_all����:" + e.getMessage());
		}
		return null;
	}
	
	//��ѯ�����׶����ϵ��
	public ResultSet check_coefficient(String mysql2) throws Exception{
		try {
			Class.forName(DBDriver);
			conn = DriverManager.getConnection(url,id,password);
			perstat = conn.prepareStatement(mysql2);
			rs = perstat.executeQuery();
			return rs;
		}
		catch(Exception e) {
			e.printStackTrace();
			System.out.println("��ѯ��analysis_phase_pearson����" + e.getMessage());
		}
		return null;
		
	}
	//��ѯԤ��׶γ�׼ȷ����ȫ������
	public ResultSet check_predict(String mysql3) throws Exception{
		try {
			Class.forName(DBDriver);
			conn = DriverManager.getConnection(url,id,password);
			perstat = conn.prepareStatement(mysql3);
			rs = perstat.executeQuery();
			return rs;
		}
		catch(Exception e) {
			e.printStackTrace();
			System.out.println("��ѯ��prediction_phase_all����" + e.getMessage());
		}
		return null;
		
	}
	//��ѯԤ��׶��㷨׼ȷ��
	public ResultSet check_predict_accuracy(String mysql4) throws Exception{
		try {
			Class.forName(DBDriver);
			conn = DriverManager.getConnection(url,id,password);
			perstat = conn.prepareStatement(mysql4);
			rs = perstat.executeQuery();
			return rs;
		}
		catch(Exception e) {
			e.printStackTrace();
			System.out.println("��ѯ��analysis_phase_pearson����" + e.getMessage());
		}
		return null;
		
	}
}
