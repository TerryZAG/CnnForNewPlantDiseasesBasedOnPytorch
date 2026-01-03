import json

def reverse_json_key_value(input_file, output_file):
    """
    反转JSON文件中的key和value
    
    Args:
        input_file (str): 输入JSON文件路径
        output_file (str): 输出JSON文件路径
    """
    try:
        # 1. 读取并解析JSON文件
        with open(input_file, 'r', encoding='utf-8') as f:
            original_data = json.load(f)
        
        # 检查数据类型是否为字典
        if not isinstance(original_data, dict):
            raise TypeError("JSON文件的顶层数据结构必须是对象（字典）")
        
        # 2. 反转键值对（处理可能的重复值）
        reversed_data = {}
        duplicate_values = []
        
        for key, value in original_data.items():
            # 确保value可以作为合法的JSON键（JSON键只能是字符串）
            new_key = str(value) if not isinstance(value, (str, int, float, bool, None)) else value
            
            if new_key in reversed_data:
                duplicate_values.append(new_key)
                # 处理重复值：可以选择覆盖/跳过/报错，这里选择覆盖并给出警告
                print(f"警告: 值 '{new_key}' 重复出现，将覆盖原有键值对")
            
            reversed_data[new_key] = key
        
        # 3. 将反转后的数据写入新的JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            # indent=4 让输出的JSON文件更易读
            json.dump(reversed_data, f, ensure_ascii=False, indent=4)
        
        print(f"JSON键值反转完成！结果已保存到: {output_file}")
        
        # 提示重复值信息
        if duplicate_values:
            print(f"注意：检测到重复值 {set(duplicate_values)}，部分数据可能被覆盖")
            
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file}'")
    except json.JSONDecodeError:
        print(f"错误：'{input_file}' 不是有效的JSON文件")
    except Exception as e:
        print(f"处理过程中出现错误：{str(e)}")

# 示例使用
if __name__ == "__main__":
    # 替换为你的输入输出文件路径
    INPUT_JSON = "lables.json"
    OUTPUT_JSON = "reversed.json"
    
    reverse_json_key_value(INPUT_JSON, OUTPUT_JSON)