class Solution {
    public String arrangeWords(String text) {
        
        String[] strArr = text.split(" ");
        Arrays.sort(strArr, (str1, str2) -> str1.length()-str2.length());
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < strArr.length; i++){
            if(i == 0){
                sb.append(strArr[i].substring(0,1).toUpperCase() + strArr[i].substring(1));
            }
            else{
                sb.append(strArr[i].toLowerCase());
            }
            sb.append(" ");
        }
        
        return sb.toString().trim();
    }
}
