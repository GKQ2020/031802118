#include<bits/stdc++.h>
using namespace std;

int cnt=0;
string all[500005];
map<string,int>Orig;
map<string,int>Plagiarism;
string s1,s2;
double lcs[500005][2]={0.0};

void build_Orig(){
	string s;
	s1="";
	while(cin>>s){
		int len=s.size();
		s1=s1+s;
		for(int i=0;i<len;i+=2){
			string a="";
			a=a+s[i]+s[i+1];
			if(Orig[a]==0){
				all[cnt++]=a;
			}
			Orig[a]++;
		}
	}
	return;
}

void build_Plagiarism(){
	Plagiarism.clear();
	string s;
	s2="";
	while(cin>>s){
		int len=s.size();
		s2=s2+s;
		for(int i=0;i<len;i+=2){
			string a="";
			a=a+s[i]+s[i+1];
			if(Orig[a]==0&&Plagiarism[a]==0){
				all[cnt++]=a;
			}
			Plagiarism[a]++;
		}
	}
	return;
}

double LCS(){
	memset(lcs,0.0,sizeof(lcs));
	int len1=s1.size();
	int len2=s2.size();
	for(int i=0,k=0;i<len1;i++,k=!k){
		for(int j=0;j<len2;j++){
			lcs[j+1][k]=max(lcs[j][!k]+(s1[i]==s2[j]?1.0:0.0),lcs[j][k]);
		}
	}
	return (double)(max(lcs[len2][1],lcs[len2][0]))/len1*0.7;
}

double Cosine(){
	double x_y=0.0;
	double x=0.0;
	double y=0.0;
	for(int i=0;i<cnt;i++){
		x_y+=(double)(Orig[all[i]]*Plagiarism[all[i]]);
		x+=(double)(Orig[all[i]]*Orig[all[i]]);
		y+=(double)(Plagiarism[all[i]]*Plagiarism[all[i]]);
	}
	return (double)(x_y/(sqrt(x)*sqrt(y))*0.3);
}

int main()
{
	int cnt=0;
	
	freopen("orig.txt","r",stdin);
	build_Orig();
	fclose(stdin);
	cin.clear();
	
	freopen("orig_0.8_add.txt","r",stdin);
//	freopen("ans1.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_add.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_del.txt","r",stdin);
//	freopen("ans2.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_del.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_dis_1.txt","r",stdin);
//	freopen("ans3.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_dis_1.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_dis_3.txt","r",stdin);
//	freopen("ans4.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_dis_3.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_dis_7.txt","r",stdin);
//	freopen("ans5.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_dis_7.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_dis_10.txt","r",stdin);
//	freopen("ans6.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_dis_10.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_dis_15.txt","r",stdin);
//	freopen("ans7.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_dis_15.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_mix.txt","r",stdin);
//	freopen("ans8.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_mix.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig_0.8_rep.txt","r",stdin);
//	freopen("ans9.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig_0.8_rep.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	freopen("orig.txt","r",stdin);
//	freopen("ans10.txt","w",stdout);
	build_Plagiarism();
	fclose(stdin);
	cin.clear();
	cout<<"开始处理orig.txt"<<endl;
	cout<<"查重率为："<<(double)(LCS()+Cosine())<<endl;
	cout<<"本次查重结束"<<endl<<endl;
	
	return 0;
}
