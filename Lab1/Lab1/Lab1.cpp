#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <malloc.h>
#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <valarray>
#include <map>
#include <list>
#include <stack>
#include <regex>

using namespace std;

ifstream f_in;
ofstream f_out;

string StrToPostfix(string str) {
	stack <const char*> StrStack;
	map<char, int>  priority_operation;
	priority_operation['*'] = 3;
	priority_operation['/'] = 3;
	priority_operation['+'] = 2;
	priority_operation['-'] = 2;
	priority_operation['('] = 1;

	vector <const char*> ListPostfix;
	map<int, string> Infix;
	vector<string> vec1;
	vector<const char*> vec2;
	string StrPostfix;
	int k = 0;
	int m = 0;

	
	while (k < str.size()) {
		/*string str1;
		m = k;
		while (isdigit(str[k]) != 0) {
			str1 += str[k];
			k++;
		}
		if (isdigit(str[m]) != 0) {
			Infix[m] = str1;
		}
		else {*/
			Infix[k] += str[k];
			k++;
		//}
	}

	for (int i = 0; i < Infix.size(); i++) {
		if (Infix[i] != "") {
			vec1.push_back(Infix[i]);
		}
	}
	

	for (int i = 0; i < vec1.size(); i++) {
		vec2.resize(vec1.size(), nullptr);

		transform(begin(vec1), end(vec1), begin(vec2), [&](const string& str)
		{
			return str.c_str();
		});
	}
 
	for (int i = 0; i < vec2.size(); i++) {
		
		if (isalpha(*vec2[i])|| isdigit(*vec2[i]) != 0 ) {
			ListPostfix.push_back(vec2[i]);
		}
		else 
			if (*vec2[i] == '(') {
			StrStack.push(vec2[i]);
		}
		else if (*vec2[i] == ')') {
			
			while(*StrStack.top() != '(') {
				const char* current = StrStack.top();
				StrStack.pop();
				if (priority_operation[*current]) {
					ListPostfix.push_back(current);
				}
				if (StrStack.size() == 0) {
					f_out << "Ошибка, неверно поставлен разделитель или не согласованы скобки";
					throw ("Ошибка, неверно поставлен разделитель или не согласованы скобки");
				}
			}
			StrStack.pop();
		}
		else if (priority_operation[*vec2[i]]) {
			while (StrStack.size() != 0 && priority_operation[*StrStack.top()] >= priority_operation[*vec2[i]]) {
				ListPostfix.push_back(StrStack.top());
				StrStack.pop();
			}
			StrStack.push(vec2[i]);
		}
	}
	while (StrStack.size() != 0) {
		if (StrStack.top() != "(" && vec2.size()>2) {
				ListPostfix.push_back(StrStack.top());
				StrStack.pop();
		}
		else {
			f_out << "Ошибка, неверно поставлен разделитель или не согласованы скобки\n";
			throw ("Ошибка, неверно поставлен разделитель или не согласованы скобки\n");
		}
	}

	for (const char* StrBuf: ListPostfix) {
		StrPostfix += StrBuf;
	}
	
	return StrPostfix;
}

map <string, double> FindOperation(string str) {
	map<string, double> operation;
	string StrBuf;
	vector <const char*> ListPostfix;
	map<int, string> Infix;
	vector<string> vec1;
	vector<const char*> vec2;
	string StrPostfix;
	int k = 0;
	int m = 0;

	//строку распределяем по символам
	while (k < str.size()) {
		/*string str1;
		m = k;
		while (isdigit(str[k]) != 0) {
			str1 += str[k];
			k++;
		}
		if (isdigit(str[m]) != 0) {
			Infix[m] = str1;
		}
		else {*/
		Infix[k] += str[k];
		k++;
		//}
	}

	for (int i = 0; i < Infix.size(); i++) {
		if (Infix[i] != "") {
			vec1.push_back(Infix[i]);
		}
	}
	for (int i = 0; i < vec1.size(); i++) {
		vec2.resize(vec1.size(), nullptr);

		transform(begin(vec1), end(vec1), begin(vec2), [&](const string& str)
		{
			return str.c_str();
		});
	}


	for (int i = 0; i < vec2.size(); i++) {
		if (isalpha(*vec2[i])) {
			if (!operation[vec2[i]]) {
				cout << vec2[i]<<"=";
				cin >> StrBuf;
				f_out << vec2[i] << " = " << StrBuf<<endl;
				double buf = stod(StrBuf);
				operation[vec2[i]] = buf;
			}
		}
		else if (isdigit(*vec2[i])) {
			double buf = stod(vec2[i]);
			operation[vec2[i]] = buf;
		}
	}
	return operation;
}


double Operator(string Operand, double operand1, double operand2) {
	double result;
	if (Operand == "*") result = operand1 * operand2;
	else if (Operand == "/") {
		if (operand2 == 0) {
			f_out << "Деление на 0 невозможно";
			throw "Деление на 0 невозможно";
		}
		result = operand1 / operand2;
	}
	else if (Operand == "+") result = operand1 + operand2;
	else if (Operand == "-") result = operand1 - operand2;
	else { 
		f_out << "Ошибка, неизвестный оператор";
		throw "Ошибка, неизвестный оператор"; }
	return result;
}

double Calculation(map <string, double>  operand, string str) {
	double result;
	stack <double> StrStack;
	vector <const char*> ListPostfix;
	map<int, string> Infix;
	vector<string> vec1;
	vector<const char*> vec2;
	string StrPostfix;
	int k = 0;
	int m = 0;

	//строку распределяем по символам
	while (k < str.size()) {
		/*string str1;
		m = k;
		while (isdigit(str[k]) != 0) {
			str1 += str[k];
			k++;
		}
		if (isdigit(str[m]) != 0) {
			Infix[m] = str1;
		}
		else {*/
		Infix[k] += str[k];
		k++;
		//}
	}

	for (int i = 0; i < Infix.size(); i++) {
		if (Infix[i] != "") {
			vec1.push_back(Infix[i]);
		}
	}
	for (int i = 0; i < vec1.size(); i++) {
		vec2.resize(vec1.size(), nullptr);

		transform(begin(vec1), end(vec1), begin(vec2), [&](const string& str)
		{
			return str.c_str();
		});
	}


	for (int i = 0; i < vec2.size(); i++) {
		if (operand[vec2[i]]) {
			StrStack.push(operand[vec2[i]]);
		}
		else {
			double operand2 = StrStack.top();
			StrStack.pop();
			if (StrStack.size() != 0) {
				double operand1 = StrStack.top();
				StrStack.pop();
				result = Operator(vec2[i], operand1, operand2);
			}else if (*vec2[i] == '-') {
				result = -operand2;
			}
			else if (*vec2[i] == '+') {
				result = operand2;
			}
			else {
				throw "Ошибка, недостаточно операндов.";
			}
			StrStack.push(result);
		}
	}
	return result;
}


int main()
{
	try
	{
		f_in.open("input.txt");
		try
		{
			f_out.open("output.txt");
			string str;
			while (getline(f_in, str)) {
				if (str == "" || str == "\n")  return 0;
				else {
					try {
						string postfix = StrToPostfix(str);
						f_out << "Исходное выражение: " <<str<< '\n';
						f_out << "Выражение в  постфиксной форме: " << postfix << '\n';
						map <string, double> operation = FindOperation(str);
						double ResultPostfix = Calculation(operation, postfix);
						f_out << "Результат вычислений в постфиксной форме: " << ResultPostfix << '\n';
						
					}
					catch (const char* exception) {
						cerr << "Error: " << exception << '\n';
					}
				}

			}
		}
		catch (std::ofstream::failure &writeErr) {
			cout << "Unable to open the output file\n";
		}		

	}
	catch (std::ifstream::failure &readErr) {
		cout << "The input data file was not opened\n";
	}
}



