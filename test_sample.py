import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class test_sort {

@Test
public void test1() {
int [] start = new int[]{7, 2, 9, 1};
int [] expected_result = temp.getResult(start);
int [] result = new int[]{1, 2, 7, 9};
assertArrayEquals(result, expected_result);
}

}