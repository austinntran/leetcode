import java.util.Arrays;

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    public static void main(String[] args) {

    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode current = head;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int val = (l1 != null ? l1.val: 0) + (l2 != null ? l2.val: 0)
                    + carry;
            carry = val >= 10 ? 1 : 0;
            ListNode node = new ListNode(val % 10);
            current.next = node;
            current = node;
            l1 = (l1 != null? l1.next: null);
            l2 = (l2 != null? l2.next: null);
        }
        return head.next;
    }
}
