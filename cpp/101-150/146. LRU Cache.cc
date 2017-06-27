class LRUCache {
private:
    int m_capability;
    unordered_map<int, list<pair<int, int>>::iterator> m_map;
    list<pair<int, int>> m_list;
public:
    LRUCache(int capacity): m_capability(capacity) {
    }

    int get(int key) {
    	auto iter = m_map.find(key);
    	if(iter == m_map.end()){
    		return -1;
    	}
    	m_list.splice(m_list.begin(), m_list, iter->second);
    	return iter->second->second;
    }

    void put(int key, int value) {
    	auto iter = m_map.find(key);
    	if(iter != m_map.end()){
    		m_list.splice(m_list.begin(), m_list, iter->second);
    		iter->second->second = valuse;
    		return;
    	}
    	if(m_list.size() == m_capability){
    		int key = m_list.back().first;
    		m_list.pop_back();
    		m_map.erase(key);
    	}
    	m_list.emplace_front(key, value);
    	m_map[key] = m_list.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */